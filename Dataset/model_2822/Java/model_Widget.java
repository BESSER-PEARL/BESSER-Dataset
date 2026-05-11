





import java.util.List;
import java.util.ArrayList;

public class model_Widget extends NoteSupport {

    private boolean locked;
    private int measuredWidth;
    private int height;
    private int measuredHeight;
    private int y;
    private String layoutParams;
    private String customData;
    private int width;
    private String text;
    private String customId;
    private boolean annotation;
    private String id;
    private int x;



    public model_Widget(
        boolean locked,        int measuredWidth,        int height,        int measuredHeight,        int y,        String layoutParams,        String customData,        int width,        String text,        String customId,        boolean annotation,        String id,        int x    ) {
        super(
        );
        this.locked = locked;
        this.measuredWidth = measuredWidth;
        this.height = height;
        this.measuredHeight = measuredHeight;
        this.y = y;
        this.layoutParams = layoutParams;
        this.customData = customData;
        this.width = width;
        this.text = text;
        this.customId = customId;
        this.annotation = annotation;
        this.id = id;
        this.x = x;
    }


    public boolean getLocked() {
        return locked;
    }

    public void setLocked(boolean locked) {
        this.locked = locked;
    }
    public int getMeasuredwidth() {
        return measuredWidth;
    }

    public void setMeasuredwidth(int measuredWidth) {
        this.measuredWidth = measuredWidth;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public int getMeasuredheight() {
        return measuredHeight;
    }

    public void setMeasuredheight(int measuredHeight) {
        this.measuredHeight = measuredHeight;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public String getLayoutparams() {
        return layoutParams;
    }

    public void setLayoutparams(String layoutParams) {
        this.layoutParams = layoutParams;
    }
    public String getCustomdata() {
        return customData;
    }

    public void setCustomdata(String customData) {
        this.customData = customData;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getCustomid() {
        return customId;
    }

    public void setCustomid(String customId) {
        this.customId = customId;
    }
    public boolean getAnnotation() {
        return annotation;
    }

    public void setAnnotation(boolean annotation) {
        this.annotation = annotation;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }


}