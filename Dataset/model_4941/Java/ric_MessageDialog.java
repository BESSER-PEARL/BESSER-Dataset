





import java.util.List;
import java.util.ArrayList;

public class ric_MessageDialog extends RichWidget {

    private String message;
    private int width;
    private int height;
    private boolean resizable;
    private String title;
    private int minWidthResize;
    private int maxWidthResize;
    private int minHeightResize;
    private boolean modal;
    private boolean autoOpen;
    private int maxHeightResize;



    public ric_MessageDialog(
        String message,        int width,        int height,        boolean resizable,        String title,        int minWidthResize,        int maxWidthResize,        int minHeightResize,        boolean modal,        boolean autoOpen,        int maxHeightResize    ) {
        super(
        );
        this.message = message;
        this.width = width;
        this.height = height;
        this.resizable = resizable;
        this.title = title;
        this.minWidthResize = minWidthResize;
        this.maxWidthResize = maxWidthResize;
        this.minHeightResize = minHeightResize;
        this.modal = modal;
        this.autoOpen = autoOpen;
        this.maxHeightResize = maxHeightResize;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
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
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getMinwidthresize() {
        return minWidthResize;
    }

    public void setMinwidthresize(int minWidthResize) {
        this.minWidthResize = minWidthResize;
    }
    public int getMaxwidthresize() {
        return maxWidthResize;
    }

    public void setMaxwidthresize(int maxWidthResize) {
        this.maxWidthResize = maxWidthResize;
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
    public boolean getAutoopen() {
        return autoOpen;
    }

    public void setAutoopen(boolean autoOpen) {
        this.autoOpen = autoOpen;
    }
    public int getMaxheightresize() {
        return maxHeightResize;
    }

    public void setMaxheightresize(int maxHeightResize) {
        this.maxHeightResize = maxHeightResize;
    }


}