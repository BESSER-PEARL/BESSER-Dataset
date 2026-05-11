





import java.util.List;
import java.util.ArrayList;

public class ric_MessageDialog extends RichWidget {

    private boolean modal;
    private int maxHeightResize;
    private int maxWidthResize;
    private int width;
    private String title;
    private String message;
    private boolean autoOpen;
    private int minHeightResize;
    private int height;
    private boolean resizable;
    private int minWidthResize;



    public ric_MessageDialog(
        boolean modal,        int maxHeightResize,        int maxWidthResize,        int width,        String title,        String message,        boolean autoOpen,        int minHeightResize,        int height,        boolean resizable,        int minWidthResize    ) {
        super(
        );
        this.modal = modal;
        this.maxHeightResize = maxHeightResize;
        this.maxWidthResize = maxWidthResize;
        this.width = width;
        this.title = title;
        this.message = message;
        this.autoOpen = autoOpen;
        this.minHeightResize = minHeightResize;
        this.height = height;
        this.resizable = resizable;
        this.minWidthResize = minWidthResize;
    }


    public boolean getModal() {
        return modal;
    }

    public void setModal(boolean modal) {
        this.modal = modal;
    }
    public int getMaxheightresize() {
        return maxHeightResize;
    }

    public void setMaxheightresize(int maxHeightResize) {
        this.maxHeightResize = maxHeightResize;
    }
    public int getMaxwidthresize() {
        return maxWidthResize;
    }

    public void setMaxwidthresize(int maxWidthResize) {
        this.maxWidthResize = maxWidthResize;
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
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public boolean getAutoopen() {
        return autoOpen;
    }

    public void setAutoopen(boolean autoOpen) {
        this.autoOpen = autoOpen;
    }
    public int getMinheightresize() {
        return minHeightResize;
    }

    public void setMinheightresize(int minHeightResize) {
        this.minHeightResize = minHeightResize;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public boolean getResizable() {
        return resizable;
    }

    public void setResizable(boolean resizable) {
        this.resizable = resizable;
    }
    public int getMinwidthresize() {
        return minWidthResize;
    }

    public void setMinwidthresize(int minWidthResize) {
        this.minWidthResize = minWidthResize;
    }


}