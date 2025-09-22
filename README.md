# PassPhrasePlus
                                                                        
                                                                        
PassPhrasePlus is a Python command-line tool to generate secure and (somewhat) memorable passwords!

Usage:

    - Without parameters, it will output 5 passphrases. Each passphrase is separated by a space and contains no special characters or numbers.

    - Using the -n flag, you can specify the number of passphrases you want generated.  
      Example:  
      input:  python3 .\passphraseplus.py -n 1  
      output: rivers are buying a chair

    - Using the -d flag followed by your specified delimiter, the passphrase words will be separated by your chosen delimiter.  
      Example:  
      input:  python3 .\passphraseplus.py -d -  
      output: pilot-grew-enough-shoe etc.

    - Using the -r flag, the output will have:  
      • the first character of a random word capitalized,  
      • a random word appended with a special character, and  
      • a random word appended with a random number.  
      Example:  
      input:  python3 .\passphraseplus.py -r  
      output: phone had) cleaned19 its Scissors etc.

    - All flags can be used together!  
      Example:  
      input:  .\passphraseplus.py -r -d +  
      output: phone+had)+cleaned19+its+Scissors etc.

    - The -h flag will show the help messages