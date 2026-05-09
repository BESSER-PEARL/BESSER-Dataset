





import java.util.List;
import java.util.ArrayList;

public class presentation_FormAttachment  {

    private String numerator;
    private String offset;
    private String denominator;
    private String mixed;
    private String alignment;
    private String group;





    private List<presentation_Control> presentation_controls;


    public presentation_FormAttachment(
        String numerator,        String offset,        String denominator,        String mixed,        String alignment,        String group    ) {
        this.numerator = numerator;
        this.offset = offset;
        this.denominator = denominator;
        this.mixed = mixed;
        this.alignment = alignment;
        this.group = group;
        this.presentation_controls = new ArrayList<>();
    }

    public presentation_FormAttachment(
        String numerator,        String offset,        String denominator,        String mixed,        String alignment,        String group        ArrayList<presentation_Control> presentation_controls    ) {
        this.numerator = numerator;
        this.offset = offset;
        this.denominator = denominator;
        this.mixed = mixed;
        this.alignment = alignment;
        this.group = group;
        this.presentation_controls = presentation_controls;
    }

    public String getNumerator() {
        return numerator;
    }

    public void setNumerator(String numerator) {
        this.numerator = numerator;
    }
    public String getOffset() {
        return offset;
    }

    public void setOffset(String offset) {
        this.offset = offset;
    }
    public String getDenominator() {
        return denominator;
    }

    public void setDenominator(String denominator) {
        this.denominator = denominator;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getAlignment() {
        return alignment;
    }

    public void setAlignment(String alignment) {
        this.alignment = alignment;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<presentation_Control> getPresentation_controls() {
        return presentation_controls;
    }

    public void addPresentation_control(Presentation_control presentation_control) {
        this.presentation_controls.add(presentation_control);
    }

}