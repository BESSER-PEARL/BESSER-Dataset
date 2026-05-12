





import java.util.List;
import java.util.ArrayList;

public class Prompt  {

    private None frameFont;
    private None frame;
    private int MAX_COMMAND_LENGTH;
    private int FONT_SIZE;
    private None commandLine;
    private None output;
    private int OUTPUT_WIDTH;
    private int OUTPUT_HEIGHT;
    private int queuePosition;





    private Operating_System operating_system;


    public Prompt(
        None frameFont,        None frame,        int MAX_COMMAND_LENGTH,        int FONT_SIZE,        None commandLine,        None output,        int OUTPUT_WIDTH,        int OUTPUT_HEIGHT,        int queuePosition    ) {
        this.frameFont = frameFont;
        this.frame = frame;
        this.MAX_COMMAND_LENGTH = MAX_COMMAND_LENGTH;
        this.FONT_SIZE = FONT_SIZE;
        this.commandLine = commandLine;
        this.output = output;
        this.OUTPUT_WIDTH = OUTPUT_WIDTH;
        this.OUTPUT_HEIGHT = OUTPUT_HEIGHT;
        this.queuePosition = queuePosition;
    }


    public None getFramefont() {
        return frameFont;
    }

    public void setFramefont(None frameFont) {
        this.frameFont = frameFont;
    }
    public None getFrame() {
        return frame;
    }

    public void setFrame(None frame) {
        this.frame = frame;
    }
    public int getMax_command_length() {
        return MAX_COMMAND_LENGTH;
    }

    public void setMax_command_length(int MAX_COMMAND_LENGTH) {
        this.MAX_COMMAND_LENGTH = MAX_COMMAND_LENGTH;
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
    public int getOutput_width() {
        return OUTPUT_WIDTH;
    }

    public void setOutput_width(int OUTPUT_WIDTH) {
        this.OUTPUT_WIDTH = OUTPUT_WIDTH;
    }
    public int getOutput_height() {
        return OUTPUT_HEIGHT;
    }

    public void setOutput_height(int OUTPUT_HEIGHT) {
        this.OUTPUT_HEIGHT = OUTPUT_HEIGHT;
    }
    public int getQueueposition() {
        return queuePosition;
    }

    public void setQueueposition(int queuePosition) {
        this.queuePosition = queuePosition;
    }

    public Operating_System getOperating_system() {
        return operating_system;
    }

    public void setOperating_system(Operating_System operating_system) {
        this.operating_system = operating_system;
    }

}