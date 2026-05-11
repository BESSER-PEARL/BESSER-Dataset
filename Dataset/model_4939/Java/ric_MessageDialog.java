





import java.util.List;
import java.util.ArrayList;

public class ric_MessageDialog extends RichWidget {

    private boolean resizable;
    private int maxHeightResize;
    private int minHeightResize;
    private boolean modal;
    private String message;
    private int minWidthResize;
    private int width;
    private String title;
    private boolean autoOpen;
    private int height;
    private int maxWidthResize;



    public ric_MessageDialog(
        boolean resizable,        int maxHeightResize,        int minHeightResize,        boolean modal,        String message,        int minWidthResize,        int width,        String title,        boolean autoOpen,        int height,        int maxWidthResize    ) {
        super(
        );
        this.resizable = resizable;
        this.maxHeightResize = maxHeightResize;
        this.minHeightResize = minHeightResize;
        this.modal = modal;
        this.message = message;
        this.minWidthResize = minWidthResize;
        this.width = width;
        this.title = title;
        this.autoOpen = autoOpen;
        this.height = height;
        this.maxWidthResize = maxWidthResize;
    }


    public boolean getResizable() {
        return resizable;
    }

    public void setResizable(boolean resizable) {
        this.resizable = resizable;
    }
    public int getMaxheightresize() {
        return maxHeightResize;
    }

    public void setMaxheightresize(int maxHeightResize) {
        this.maxHeightResize = maxHeightResize;
    }
    public int getMinheightresize() {
        return minHeightResize;
    }

    public void setMinheightresize(int minHeightResize) {
        this.minHeightResize = minHeightResize;
    }
    public boolean getModal() {
        return modal;
    }

    public void setModal(boolean modal) {
        this.modal = modal;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public int getMinwidthresize() {
        return minWidthResize;
    }

    public void setMinwidthresize(int minWidthResize) {
        this.minWidthResize = minWidthResize;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public boolean getAutoopen() {
        return autoOpen;
    }

    public void setAutoopen(boolean autoOpen) {
        this.autoOpen = autoOpen;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public int getMaxwidthresize() {
        return maxWidthResize;
    }

    public void setMaxwidthresize(int maxWidthResize) {
        this.maxWidthResize = maxWidthResize;
    }


}