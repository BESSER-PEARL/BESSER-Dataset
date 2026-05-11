





import java.util.List;
import java.util.ArrayList;

public class JavaMM_Container extends Type {

    private String type;





    private JavaMM_Program javamm_program;




    private JavaMM_Type javamm_type;


    public JavaMM_Container(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public JavaMM_Program getJavamm_program() {
        return javamm_program;
    }

    public void setJavamm_program(JavaMM_Program javamm_program) {
        this.javamm_program = javamm_program;
    }
    public JavaMM_Type getJavamm_type() {
        return javamm_type;
    }

    public void setJavamm_type(JavaMM_Type javamm_type) {
        this.javamm_type = javamm_type;
    }

}