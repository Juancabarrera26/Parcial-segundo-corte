import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

public class Main {
    public static void main(String[] args) throws Exception {

        // Entrada de prueba (puedes cambiarla)
        String input = "INSERTAR usuarios ( nombre = \"Juan Camilo\"; edad = 20 )";

        // Crear flujo de caracteres
        CharStream entrada = CharStreams.fromString(input);

        // Analizador lexico
        CRUDSimpleLexer lexer = new CRUDSimpleLexer(entrada);

        // Flujo de tokens
        CommonTokenStream tokens = new CommonTokenStream(lexer);

        // Parser
        CRUDSimpleParser parser = new CRUDSimpleParser(tokens);

        // Regla inicial
        ParseTree arbol = parser.programa();

        // Mostrar arbol
        System.out.println(arbol.toStringTree(parser));
    }
}
