





import java.util.List;
import java.util.ArrayList;

public class r1_Code extends Expression {

    private String code;
    private String display;





    private r1_CodeSystemRef r1_codesystemref;




    private r1_Concept r1_concept;


    public r1_Code(
        String code,        String display    ) {
        super(
        );
        this.code = code;
        this.display = display;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getDisplay() {
        return display;
    }

    public void setDisplay(String display) {
        this.display = display;
    }

    public r1_CodeSystemRef getR1_codesystemref() {
        return r1_codesystemref;
    }

    public void setR1_codesystemref(r1_CodeSystemRef r1_codesystemref) {
        this.r1_codesystemref = r1_codesystemref;
    }
    public r1_Concept getR1_concept() {
        return r1_concept;
    }

    public void setR1_concept(r1_Concept r1_concept) {
        this.r1_concept = r1_concept;
    }

}