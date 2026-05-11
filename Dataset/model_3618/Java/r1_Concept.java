





import java.util.List;
import java.util.ArrayList;

public class r1_Concept extends Expression {

    private String display;





    private List<r1_Code> r1_codes;


    public r1_Concept(
        String display    ) {
        super(
        );
        this.display = display;
        this.r1_codes = new ArrayList<>();
    }

    public r1_Concept(
        String display        ArrayList<r1_Code> r1_codes    ) {
        this.display = display;
        this.r1_codes = r1_codes;
    }

    public String getDisplay() {
        return display;
    }

    public void setDisplay(String display) {
        this.display = display;
    }

    public List<r1_Code> getR1_codes() {
        return r1_codes;
    }

    public void addR1_code(R1_code r1_code) {
        this.r1_codes.add(r1_code);
    }

}