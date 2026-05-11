





import java.util.List;
import java.util.ArrayList;

public class picojava_TypeDecl extends Decl {

    private boolean isQualified;





    private picojava_Program picojava_program;


    public picojava_TypeDecl(
        boolean isQualified    ) {
        super(
        );
        this.isQualified = isQualified;
    }


    public boolean getIsqualified() {
        return isQualified;
    }

    public void setIsqualified(boolean isQualified) {
        this.isQualified = isQualified;
    }

    public picojava_Program getPicojava_program() {
        return picojava_program;
    }

    public void setPicojava_program(picojava_Program picojava_program) {
        this.picojava_program = picojava_program;
    }

}