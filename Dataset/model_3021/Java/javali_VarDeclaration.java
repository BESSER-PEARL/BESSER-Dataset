





import java.util.List;
import java.util.ArrayList;

public class javali_VarDeclaration extends Statement {






    private javali_Identifier javali_identifier;




    private javali_Type javali_type;


    public javali_VarDeclaration(
    ) {
        super(
        );
    }



    public javali_Identifier getJavali_identifier() {
        return javali_identifier;
    }

    public void setJavali_identifier(javali_Identifier javali_identifier) {
        this.javali_identifier = javali_identifier;
    }
    public javali_Type getJavali_type() {
        return javali_type;
    }

    public void setJavali_type(javali_Type javali_type) {
        this.javali_type = javali_type;
    }

}