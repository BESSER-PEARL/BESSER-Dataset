





import java.util.List;
import java.util.ArrayList;

public class Prompt  {

    private int FONT_SIZE;
    private None commandLine;
    private None output;
    private None frameFont;





    private Operating_System operating_system;


    public Prompt(
        int FONT_SIZE,        None commandLine,        None output,        None frameFont    ) {
        this.FONT_SIZE = FONT_SIZE;
        this.commandLine = commandLine;
        this.output = output;
        this.frameFont = frameFont;
    }


    public int getFont_size() {
        return FONT_SIZE;
    }

    public void setFont_size(int FONT_SIZE) {
        this.FONT_SIZE = FONT_SIZE;
    }
    public None getCommandline() {
        return commandLine;
    }

    public void setCommandline(None commandLine) {
        this.commandLine = commandLine;
    }
    public None getOutput() {
        return output;
    }

    public void setOutput(None output) {
        this.output = output;
    }
    public None getFramefont() {
        return frameFont;
    }

    public void setFramefont(None frameFont) {
        this.frameFont = frameFont;
    }

    public Operating_System getOperating_system() {
        return operating_system;
    }

    public void setOperating_system(Operating_System operating_system) {
        this.operating_system = operating_system;
    }

}