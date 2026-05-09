





import java.util.List;
import java.util.ArrayList;

public class presentation_TrayDialog extends Dialog {

    private String helpAvailable;
    private String group2;





    private List<presentation_DialogTray> presentation_dialogtrays;


    public presentation_TrayDialog(
        String helpAvailable,        String group2    ) {
        super(
        );
        this.helpAvailable = helpAvailable;
        this.group2 = group2;
        this.presentation_dialogtrays = new ArrayList<>();
    }

    public presentation_TrayDialog(
        String helpAvailable,        String group2        ArrayList<presentation_DialogTray> presentation_dialogtrays    ) {
        this.helpAvailable = helpAvailable;
        this.group2 = group2;
        this.presentation_dialogtrays = presentation_dialogtrays;
    }

    public String getHelpavailable() {
        return helpAvailable;
    }

    public void setHelpavailable(String helpAvailable) {
        this.helpAvailable = helpAvailable;
    }
    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }

    public List<presentation_DialogTray> getPresentation_dialogtrays() {
        return presentation_dialogtrays;
    }

    public void addPresentation_dialogtray(Presentation_dialogtray presentation_dialogtray) {
        this.presentation_dialogtrays.add(presentation_dialogtray);
    }

}