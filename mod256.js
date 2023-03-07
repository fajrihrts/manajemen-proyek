const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function encrypt(plaintext, key) {
  /**
   * Melakukan enkripsi plaintext menggunakan kunci key.
   */
  let ciphertext = "";
  for (let i = 0; i < plaintext.length; i++) {
    // Convert to numeric value
    let char_num = plaintext.charCodeAt(i);
    // Apply Caesar cipher transformation
    let new_char_num = (char_num + key) % 256;
    // Convert back to character
    let new_char = String.fromCharCode(new_char_num);
    ciphertext += new_char;
  }
  return ciphertext;
}

function decrypt(ciphertext, key) {
  /**
   * Melakukan dekripsi ciphertext menggunakan kunci key.
   */
  let plaintext = "";
  for (let i = 0; i < ciphertext.length; i++) {
    // Convert to numeric value
    let char_num = ciphertext.charCodeAt(i);
    // Apply inverse Caesar cipher transformation
    let new_char_num = (char_num - key + 256) % 256;
    // Convert back to character
    let new_char = String.fromCharCode(new_char_num);
    plaintext += new_char;
  }
  return plaintext;
}

rl.question("Masukkan plaintext: ", (plaintext) => {
  rl.question("Masukkan kunci enkripsi: ", (key) => {
    // Test the functions
    let ciphertext = encrypt(plaintext, parseInt(key));
    let decrypted_text = decrypt(ciphertext, parseInt(key));

    // Print the results
    console.log("Plaintext: ", plaintext);
    console.log("Ciphertext: ", ciphertext);
    console.log("Decrypted text: ", decrypted_text);

    rl.close();
  });
});
