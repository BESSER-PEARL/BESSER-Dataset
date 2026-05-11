





import java.util.List;
import java.util.ArrayList;

public class parameterizedExpressionsTestLanguage_FunctionDeclaration extends Statement {

    private boolean generator;
    private String name;



    public parameterizedExpressionsTestLanguage_FunctionDeclaration(
        boolean generator,        String name    ) {
        super(
        );
        this.generator = generator;
        this.name = name;
    }


    public boolean getGenerator() {
        return generator;
    }

    public void setGenerator(boolean generator) {
        this.generator = generator;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}