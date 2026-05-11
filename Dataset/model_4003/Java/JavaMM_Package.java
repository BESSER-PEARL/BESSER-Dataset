





import java.util.List;
import java.util.ArrayList;

public class JavaMM_Package  {

    private String name;





    private JavaMM_Program javamm_program;


    public JavaMM_Package(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public JavaMM_Program getJavamm_program() {
        return javamm_program;
    }

    public void setJavamm_program(JavaMM_Program javamm_program) {
        this.javamm_program = javamm_program;
    }

}