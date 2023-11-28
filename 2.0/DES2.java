import java.util.Scanner;
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;

public class DES2 {
    public static void main(String[] argv) {
        System.out.println("Message Encryption Using DES Algorithm\n-------");

        // Get the message from the user
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the message: ");
        String userMessage = scanner.nextLine();
        byte[] text = userMessage.getBytes();

        try {
            KeyGenerator keygenerator = KeyGenerator.getInstance("DES");
            SecretKey myDesKey = keygenerator.generateKey();

            Cipher desCipher;
            desCipher = Cipher.getInstance("DES/ECB/PKCS5Padding");

            desCipher.init(Cipher.ENCRYPT_MODE, myDesKey);
            System.out.println("Message [Byte Format] : " + text);
            System.out.println("Message : " + new String(text));

            byte[] textEncrypted = desCipher.doFinal(text);
            System.out.println("Encrypted Message: " + textEncrypted);

            desCipher.init(Cipher.DECRYPT_MODE, myDesKey);
            byte[] textDecrypted = desCipher.doFinal(textEncrypted);
            System.out.println("Decrypted Message: " + new String(textDecrypted));

            scanner.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
