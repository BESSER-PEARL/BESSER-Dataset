





import java.util.List;
import java.util.ArrayList;

public class presentation_NotesType  {

    private String pageLayoutName;
    private String useFooterName;
    private String styleName;
    private String useDateTimeName;
    private String shape;
    private String useHeaderName;





    private presentation_FormsType presentation_formstype;




    private List<presentation_RectType> presentation_recttypes;


    public presentation_NotesType(
        String pageLayoutName,        String useFooterName,        String styleName,        String useDateTimeName,        String shape,        String useHeaderName    ) {
        this.pageLayoutName = pageLayoutName;
        this.useFooterName = useFooterName;
        this.styleName = styleName;
        this.useDateTimeName = useDateTimeName;
        this.shape = shape;
        this.useHeaderName = useHeaderName;
        this.presentation_recttypes = new ArrayList<>();
    }

    public presentation_NotesType(
        String pageLayoutName,        String useFooterName,        String styleName,        String useDateTimeName,        String shape,        String useHeaderName        ArrayList<presentation_RectType> presentation_recttypes    ) {
        this.pageLayoutName = pageLayoutName;
        this.useFooterName = useFooterName;
        this.styleName = styleName;
        this.useDateTimeName = useDateTimeName;
        this.shape = shape;
        this.useHeaderName = useHeaderName;
        this.presentation_recttypes = presentation_recttypes;
    }

    public String getPagelayoutname() {
        return pageLayoutName;
    }

    public void setPagelayoutname(String pageLayoutName) {
        this.pageLayoutName = pageLayoutName;
    }
    public String getUsefootername() {
        return useFooterName;
    }

    public void setUsefootername(String useFooterName) {
        this.useFooterName = useFooterName;
    }
    public String getStylename() {
        return styleName;
    }

    public void setStylename(String styleName) {
        this.styleName = styleName;
    }
    public String getUsedatetimename() {
        return useDateTimeName;
    }

    public void setUsedatetimename(String useDateTimeName) {
        this.useDateTimeName = useDateTimeName;
    }
    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }
    public String getUseheadername() {
        return useHeaderName;
    }

    public void setUseheadername(String useHeaderName) {
        this.useHeaderName = useHeaderName;
    }

    public presentation_FormsType getPresentation_formstype() {
        return presentation_formstype;
    }

    public void setPresentation_formstype(presentation_FormsType presentation_formstype) {
        this.presentation_formstype = presentation_formstype;
    }
    public List<presentation_RectType> getPresentation_recttypes() {
        return presentation_recttypes;
    }

    public void addPresentation_recttype(Presentation_recttype presentation_recttype) {
        this.presentation_recttypes.add(presentation_recttype);
    }

}