





import java.util.List;
import java.util.ArrayList;

public class model_Widget extends NoteSupport {

    private String id;
    private int y;
    private boolean locked;
    private int x;
    private String layoutParams;
    private int width;
    private String customData;
    private int measuredWidth;
    private boolean annotation;
    private String text;
    private int measuredHeight;
    private String customId;
    private int height;



    public model_Widget(
        String id,        int y,        boolean locked,        int x,        String layoutParams,        int width,        String customData,        int measuredWidth,        boolean annotation,        String text,        int measuredHeight,        String customId,        int height    ) {
        super(
        );
        this.id = id;
        this.y = y;
        this.locked = locked;
        this.x = x;
        this.layoutParams = layoutParams;
        this.width = width;
        this.customData = customData;
        this.measuredWidth = measuredWidth;
        this.annotation = annotation;
        this.text = text;
        this.measuredHeight = measuredHeight;
        this.customId = customId;
        this.height = height;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public boolean getLocked() {
        return locked;
    }

    public void setLocked(boolean locked) {
        this.locked = locked;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public String getLayoutparams() {
        return layoutParams;
    }

    public void setLayoutparams(String layoutParams) {
        this.layoutParams = layoutParams;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public String getCustomdata() {
        return customData;
    }

    public void setCustomdata(String customData) {
        this.customData = customData;
    }
    public int getMeasuredwidth() {
        return measuredWidth;
    }

    public void setMeasuredwidth(int measuredWidth) {
        this.measuredWidth = measuredWidth;
    }
    public boolean getAnnotation() {
        return annotation;
    }

    public void setAnnotation(boolean annotation) {
        this.annotation = annotation;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public int getMeasuredheight() {
        return measuredHeight;
    }

    public void setMeasuredheight(int measuredHeight) {
        this.measuredHeight = measuredHeight;
    }
    public String getCustomid() {
        return customId;
    }

    public void setCustomid(String customId) {
        this.customId = customId;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }


}