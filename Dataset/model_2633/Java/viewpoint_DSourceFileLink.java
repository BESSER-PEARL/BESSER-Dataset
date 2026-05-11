





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DSourceFileLink extends DNavigationLink {

    private int endPosition;
    private int startPosition;
    private String filePath;



    public viewpoint_DSourceFileLink(
        int endPosition,        int startPosition,        String filePath    ) {
        super(
        );
        this.endPosition = endPosition;
        this.startPosition = startPosition;
        this.filePath = filePath;
    }


    public int getEndposition() {
        return endPosition;
    }

    public void setEndposition(int endPosition) {
        this.endPosition = endPosition;
    }
    public int getStartposition() {
        return startPosition;
    }

    public void setStartposition(int startPosition) {
        this.startPosition = startPosition;
    }
    public String getFilepath() {
        return filePath;
    }

    public void setFilepath(String filePath) {
        this.filePath = filePath;
    }


}