





import java.util.List;
import java.util.ArrayList;

public class presentation_FormData  {

    private String mixed;
    private String width;
    private String group;
    private String height;





    private List<presentation_FormAttachment> presentation_formattachments;




    private List<presentation_FormAttachment> presentation_formattachments;




    private List<presentation_FormAttachment> presentation_formattachments;




    private List<presentation_FormAttachment> presentation_formattachments;


    public presentation_FormData(
        String mixed,        String width,        String group,        String height    ) {
        this.mixed = mixed;
        this.width = width;
        this.group = group;
        this.height = height;
        this.presentation_formattachments = new ArrayList<>();
        this.presentation_formattachments = new ArrayList<>();
        this.presentation_formattachments = new ArrayList<>();
        this.presentation_formattachments = new ArrayList<>();
    }

    public presentation_FormData(
        String mixed,        String width,        String group,        String height        ArrayList<presentation_FormAttachment> presentation_formattachments,        ArrayList<presentation_FormAttachment> presentation_formattachments,        ArrayList<presentation_FormAttachment> presentation_formattachments,        ArrayList<presentation_FormAttachment> presentation_formattachments    ) {
        this.mixed = mixed;
        this.width = width;
        this.group = group;
        this.height = height;
        this.presentation_formattachments = presentation_formattachments;
        this.presentation_formattachments = presentation_formattachments;
        this.presentation_formattachments = presentation_formattachments;
        this.presentation_formattachments = presentation_formattachments;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }

    public List<presentation_FormAttachment> getPresentation_formattachments() {
        return presentation_formattachments;
    }

    public void addPresentation_formattachment(Presentation_formattachment presentation_formattachment) {
        this.presentation_formattachments.add(presentation_formattachment);
    }
    public List<presentation_FormAttachment> getPresentation_formattachments() {
        return presentation_formattachments;
    }

    public void addPresentation_formattachment(Presentation_formattachment presentation_formattachment) {
        this.presentation_formattachments.add(presentation_formattachment);
    }
    public List<presentation_FormAttachment> getPresentation_formattachments() {
        return presentation_formattachments;
    }

    public void addPresentation_formattachment(Presentation_formattachment presentation_formattachment) {
        this.presentation_formattachments.add(presentation_formattachment);
    }
    public List<presentation_FormAttachment> getPresentation_formattachments() {
        return presentation_formattachments;
    }

    public void addPresentation_formattachment(Presentation_formattachment presentation_formattachment) {
        this.presentation_formattachments.add(presentation_formattachment);
    }

}