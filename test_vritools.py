import unittest, os
from vritools.mutation_code import MutationCode
from vritools.mutate_fasta import mutate_fasta

class TestVRITools(unittest.TestCase):

    def test_valid_code(self):
        test_cases = [
            ('Ala23Thr', 'Ala', 23, 'Thr', 'A23T'),
            ('p.Arg23Tyr', 'Arg', 23, 'Tyr', 'R23Y'),
            ('ARG3THR', 'ARG', 3, 'THR', 'R3T')
        ]

        for code, wtres, pos, msres, concise in test_cases:
            with self.subTest(code=code):
                mutation = MutationCode(code)
                self.assertEqual(mutation.get_wtres(), wtres)
                self.assertEqual(mutation.get_pos(), pos)
                self.assertEqual(mutation.get_msres(), msres)
                self.assertEqual(mutation.concise_format(), concise)

    def test_invalid_code(self):
        with self.assertRaises(ValueError):
            MutationCode('invalid')

    def test_invalid_amino_acid(self):
        mutation = MutationCode('Xyz23Yza')
        self.assertEqual(mutation.concise_format(), 'Invalid code')
    
    def test_mutate_fasta(self):
        # Define test input and output
        fasta_file = 'P05067.fasta'  # Assume test.fasta is a valid FASTA file in the current directory
        mutation_code = 'Ala6Thr'
        output_folder = 'output'
        expected_output_file = os.path.join(output_folder, 'P05067_Ala6Thr.fasta')
        
        # Run the mutate_fasta function
        mutate_fasta(fasta_file, mutation_code, output_folder)
        
        # Check that the output file was created
        self.assertTrue(os.path.exists(expected_output_file))
        
        # Read the mutated sequence from the output file
        with open(expected_output_file, 'r') as f:
            mutated_sequence = ''.join(f.readlines()[1:]).replace('\n', '')
        
        # Assume the original sequence is known for this test
        with open(r'/Users/murto/Documents/Code/tcag/3_vritools/P05067.fasta', 'r') as f:
            original_sequence = ''.join(f.readlines()[1:]).replace('\n', '')

        expected_mutated_sequence = original_sequence[:5] + 'T' + original_sequence[6:]
        
        # Check the mutated sequence
        self.assertEqual(mutated_sequence, expected_mutated_sequence)
        
        # Clean up (delete the output folder and its contents)
        os.remove(expected_output_file)
        os.rmdir(output_folder)
    
    def test_concise_format(self):
        test_cases = [
            ('Ala23Thr', 'A23T', ('A', 23, 'T')),
            ('p.Arg23Tyr', 'R23Y', ('R', 23, 'Y')),
            ('ARG3THR', 'R3T', ('R', 3, 'T')),
        ]

        for code, concise, concise_tuple in test_cases:
            with self.subTest(code=code):
                mutation = MutationCode(code)
                self.assertEqual(mutation.concise_format(), concise)
                self.assertEqual(mutation.concise_format(as_tuple=True), concise_tuple)


if __name__ == '__main__':
    unittest.main()
