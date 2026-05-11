





import java.util.List;
import java.util.ArrayList;

public class ric_MessageDialog extends RichWidget {

    private int height;
    private String title;
    private int maxWidthResize;
    private int minWidthResize;
    private int minHeightResize;
    private int maxHeightResize;
    private boolean modal;
    private boolean autoOpen;
    private String message;
    private boolean resizable;
    private int width;



    public ric_MessageDialog(
        int height,        String title,        int maxWidthResize,        int minWidthResize,        int minHeightResize,        int maxHeightResize,        boolean modal,        boolean autoOpen,        String message,        boolean resizable,        int width    ) {
        super(
        );
        this.height = height;
        this.title = title;
        this.maxWidthResize = maxWidthResize;
        this.minWidthResize = minWidthResize;
        this.minHeightResize = minHeightResize;
        this.maxHeightResize = maxHeightResize;
        this.modal = modal;
        this.autoOpen = autoOpen;
        this.message = message;
        this.resizable = resizable;
        this.width = width;
    }


    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getMaxwidthresize() {
        return maxWidthResize;
    }

    public void setMaxwidthresize(int maxWidthResize) {
        this.maxWidthResize = maxWidthResize;
    }
    public int getMinwidthresize() {
        return minWidthResize;
    }

    public void setMinwidthresize(int minWidthResize) {
        this.minWidthResize = minWidthResize;
    }
    public int getMinheightresize() {
        return minHeightResize;
    }

    public void setMinheightresize(int minHeightResize) {
        this.minHeightResize = minHeightResize;
    }
    public int getMaxheightresize() {
        return maxHeightResize;
    }

    public void setMaxheightresize(int maxHeightResize) {
        this.maxHeightResize = maxHeightResize;
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
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public boolean getResizable() {
        return resizable;
    }

    public void setResizable(boolean resizable) {
        this.resizable = resizable;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }


}