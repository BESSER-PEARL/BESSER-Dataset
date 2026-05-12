





import java.util.List;
import java.util.ArrayList;

public class Prompt  {

    private int FONT_SIZE;
    private int OUTPUT_WIDTH;
    private int queuePosition;
    private None frame;
    private int OUTPUT_HEIGHT;
    private None output;
    private None commandLine;
    private None frameFont;
    private int MAX_COMMAND_LENGTH;





    private Operating_System operating_system;


    public Prompt(
        int FONT_SIZE,        int OUTPUT_WIDTH,        int queuePosition,        None frame,        int OUTPUT_HEIGHT,        None output,        None commandLine,        None frameFont,        int MAX_COMMAND_LENGTH    ) {
        this.FONT_SIZE = FONT_SIZE;
        this.OUTPUT_WIDTH = OUTPUT_WIDTH;
        this.queuePosition = queuePosition;
        this.frame = frame;
        this.OUTPUT_HEIGHT = OUTPUT_HEIGHT;
        this.output = output;
        this.commandLine = commandLine;
        this.frameFont = frameFont;
        this.MAX_COMMAND_LENGTH = MAX_COMMAND_LENGTH;
    }


    public int getFont_size() {
        return FONT_SIZE;
    }

    public void setFont_size(int FONT_SIZE) {
        this.FONT_SIZE = FONT_SIZE;
    }
    public int getOutput_width() {
        return OUTPUT_WIDTH;
    }

    public void setOutput_width(int OUTPUT_WIDTH) {
        this.OUTPUT_WIDTH = OUTPUT_WIDTH;
    }
    public int getQueueposition() {
        return queuePosition;
    }

    public void setQueueposition(int queuePosition) {
        this.queuePosition = queuePosition;
    }
    public None getFrame() {
        return frame;
    }

    public void setFrame(None frame) {
        this.frame = frame;
    }
    public int getOutput_height() {
        return OUTPUT_HEIGHT;
    }

    public void setOutput_height(int OUTPUT_HEIGHT) {
        this.OUTPUT_HEIGHT = OUTPUT_HEIGHT;
    }
    public None getOutput() {
        return output;
    }

    public void setOutput(None output) {
        this.output = output;
    }
    public None getCommandline() {
        return commandLine;
    }

    public void setCommandline(None commandLine) {
        this.commandLine = commandLine;
    }
    public None getFramefont() {
        return frameFont;
    }

    public void setFramefont(None frameFont) {
        this.frameFont = frameFont;
    }
    public int getMax_command_length() {
        return MAX_COMMAND_LENGTH;
    }

    public void setMax_command_length(int MAX_COMMAND_LENGTH) {
        this.MAX_COMMAND_LENGTH = MAX_COMMAND_LENGTH;
    }

    public Operating_System getOperating_system() {
        return operating_system;
    }

    public void setOperating_system(Operating_System operating_system) {
        this.operating_system = operating_system;
    }

}