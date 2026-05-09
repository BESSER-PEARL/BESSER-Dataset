





import java.util.List;
import java.util.ArrayList;

public class presentation_TitleAreaDialog extends TrayDialog {

    private String errorMessage;
    private String titleImage;
    private String message;
    private String title;
    private String group3;





    private List<presentation_RGB> presentation_rgbs;


    public presentation_TitleAreaDialog(
        String errorMessage,        String titleImage,        String message,        String title,        String group3    ) {
        super(
        );
        this.errorMessage = errorMessage;
        this.titleImage = titleImage;
        this.message = message;
        this.title = title;
        this.group3 = group3;
        this.presentation_rgbs = new ArrayList<>();
    }

    public presentation_TitleAreaDialog(
        String errorMessage,        String titleImage,        String message,        String title,        String group3        ArrayList<presentation_RGB> presentation_rgbs    ) {
        this.errorMessage = errorMessage;
        this.titleImage = titleImage;
        this.message = message;
        this.title = title;
        this.group3 = group3;
        this.presentation_rgbs = presentation_rgbs;
    }

    public String getErrormessage() {
        return errorMessage;
    }

    public void setErrormessage(String errorMessage) {
        this.errorMessage = errorMessage;
    }
    public String getTitleimage() {
        return titleImage;
    }

    public void setTitleimage(String titleImage) {
        this.titleImage = titleImage;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }

    public List<presentation_RGB> getPresentation_rgbs() {
        return presentation_rgbs;
    }

    public void addPresentation_rgb(Presentation_rgb presentation_rgb) {
        this.presentation_rgbs.add(presentation_rgb);
    }

}