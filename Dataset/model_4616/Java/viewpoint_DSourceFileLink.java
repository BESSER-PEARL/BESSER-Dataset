





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DSourceFileLink extends DNavigationLink {

    private int startPosition;
    private int endPosition;
    private String filePath;



    public viewpoint_DSourceFileLink(
        int startPosition,        int endPosition,        String filePath    ) {
        super(
        );
        this.startPosition = startPosition;
        this.endPosition = endPosition;
        this.filePath = filePath;
    }


    public int getStartposition() {
        return startPosition;
    }

    public void setStartposition(int startPosition) {
        this.startPosition = startPosition;
    }
    public int getEndposition() {
        return endPosition;
    }

    public void setEndposition(int endPosition) {
        this.endPosition = endPosition;
    }
    public String getFilepath() {
        return filePath;
    }

    public void setFilepath(String filePath) {
        this.filePath = filePath;
    }


}