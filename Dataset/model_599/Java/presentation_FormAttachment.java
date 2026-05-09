





import java.util.List;
import java.util.ArrayList;

public class presentation_FormAttachment  {

    private String numerator;
    private String mixed;
    private String offset;
    private String denominator;
    private String group;
    private String alignment;





    private presentation_FormData presentation_formdata;




    private presentation_FormData presentation_formdata;




    private List<presentation_Control> presentation_controls;




    private presentation_FormData presentation_formdata;




    private presentation_FormData presentation_formdata;


    public presentation_FormAttachment(
        String numerator,        String mixed,        String offset,        String denominator,        String group,        String alignment    ) {
        this.numerator = numerator;
        this.mixed = mixed;
        this.offset = offset;
        this.denominator = denominator;
        this.group = group;
        this.alignment = alignment;
        this.presentation_controls = new ArrayList<>();
    }

    public presentation_FormAttachment(
        String numerator,        String mixed,        String offset,        String denominator,        String group,        String alignment        ArrayList<presentation_Control> presentation_controls    ) {
        this.numerator = numerator;
        this.mixed = mixed;
        this.offset = offset;
        this.denominator = denominator;
        this.group = group;
        this.alignment = alignment;
        this.presentation_controls = presentation_controls;
    }

    public String getNumerator() {
        return numerator;
    }

    public void setNumerator(String numerator) {
        this.numerator = numerator;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
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
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getAlignment() {
        return alignment;
    }

    public void setAlignment(String alignment) {
        this.alignment = alignment;
    }

    public presentation_FormData getPresentation_formdata() {
        return presentation_formdata;
    }

    public void setPresentation_formdata(presentation_FormData presentation_formdata) {
        this.presentation_formdata = presentation_formdata;
    }
    public presentation_FormData getPresentation_formdata() {
        return presentation_formdata;
    }

    public void setPresentation_formdata(presentation_FormData presentation_formdata) {
        this.presentation_formdata = presentation_formdata;
    }
    public List<presentation_Control> getPresentation_controls() {
        return presentation_controls;
    }

    public void addPresentation_control(Presentation_control presentation_control) {
        this.presentation_controls.add(presentation_control);
    }
    public presentation_FormData getPresentation_formdata() {
        return presentation_formdata;
    }

    public void setPresentation_formdata(presentation_FormData presentation_formdata) {
        this.presentation_formdata = presentation_formdata;
    }
    public presentation_FormData getPresentation_formdata() {
        return presentation_formdata;
    }

    public void setPresentation_formdata(presentation_FormData presentation_formdata) {
        this.presentation_formdata = presentation_formdata;
    }

}