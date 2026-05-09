





import java.util.List;
import java.util.ArrayList;

public class ryz_PresentationFormElement  {

    private String labelText;





    private ryz_PresentationForm ryz_presentationform;


    public ryz_PresentationFormElement(
        String labelText    ) {
        this.labelText = labelText;
    }


    public String getLabeltext() {
        return labelText;
    }

    public void setLabeltext(String labelText) {
        this.labelText = labelText;
    }

    public ryz_PresentationForm getRyz_presentationform() {
        return ryz_presentationform;
    }

    public void setRyz_presentationform(ryz_PresentationForm ryz_presentationform) {
        this.ryz_presentationform = ryz_presentationform;
    }

}