





import java.util.List;
import java.util.ArrayList;

public class model_Widget extends VisibleSupport, NoteSupport, NameSupport {

    private String text;
    private String customId;
    private int x;
    private boolean locked;
    private int y;
    private String id;
    private String customData;
    private boolean annotation;
    private String layoutParams;
    private int measuredHeight;
    private int width;
    private int measuredWidth;
    private int height;



    public model_Widget(
        String text,        String customId,        int x,        boolean locked,        int y,        String id,        String customData,        boolean annotation,        String layoutParams,        int measuredHeight,        int width,        int measuredWidth,        int height    ) {
        super(
        );
        this.text = text;
        this.customId = customId;
        this.x = x;
        this.locked = locked;
        this.y = y;
        this.id = id;
        this.customData = customData;
        this.annotation = annotation;
        this.layoutParams = layoutParams;
        this.measuredHeight = measuredHeight;
        this.width = width;
        this.measuredWidth = measuredWidth;
        this.height = height;
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
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public boolean getLocked() {
        return locked;
    }

    public void setLocked(boolean locked) {
        this.locked = locked;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getCustomdata() {
        return customData;
    }

    public void setCustomdata(String customData) {
        this.customData = customData;
    }
    public boolean getAnnotation() {
        return annotation;
    }

    public void setAnnotation(boolean annotation) {
        this.annotation = annotation;
    }
    public String getLayoutparams() {
        return layoutParams;
    }

    public void setLayoutparams(String layoutParams) {
        this.layoutParams = layoutParams;
    }
    public int getMeasuredheight() {
        return measuredHeight;
    }

    public void setMeasuredheight(int measuredHeight) {
        this.measuredHeight = measuredHeight;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
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


}