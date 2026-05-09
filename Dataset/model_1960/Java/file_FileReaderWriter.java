





import java.util.List;
import java.util.ArrayList;

public class file_FileReaderWriter extends FileHandler {

    private boolean Open;
    private String CloseFeedback;
    private String WriteFeedback;
    private String ReadFeedback;



    public file_FileReaderWriter(
        boolean Open,        String CloseFeedback,        String WriteFeedback,        String ReadFeedback    ) {
        super(
        );
        this.Open = Open;
        this.CloseFeedback = CloseFeedback;
        this.WriteFeedback = WriteFeedback;
        this.ReadFeedback = ReadFeedback;
    }


    public boolean getOpen() {
        return Open;
    }

    public void setOpen(boolean Open) {
        this.Open = Open;
    }
    public String getClosefeedback() {
        return CloseFeedback;
    }

    public void setClosefeedback(String CloseFeedback) {
        this.CloseFeedback = CloseFeedback;
    }
    public String getWritefeedback() {
        return WriteFeedback;
    }

    public void setWritefeedback(String WriteFeedback) {
        this.WriteFeedback = WriteFeedback;
    }
    public String getReadfeedback() {
        return ReadFeedback;
    }

    public void setReadfeedback(String ReadFeedback) {
        this.ReadFeedback = ReadFeedback;
    }


}