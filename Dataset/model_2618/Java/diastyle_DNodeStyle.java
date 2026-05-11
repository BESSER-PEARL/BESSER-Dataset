





import java.util.List;
import java.util.ArrayList;

public class diastyle_DNodeStyle extends DNodeEdgeStyle {

    private String figure;
    private String shape;
    private String layout;
    private String shapeData;
    private int sizeY;
    private int radius;
    private int sizeX;



    public diastyle_DNodeStyle(
        String figure,        String shape,        String layout,        String shapeData,        int sizeY,        int radius,        int sizeX    ) {
        super(
        );
        this.figure = figure;
        this.shape = shape;
        this.layout = layout;
        this.shapeData = shapeData;
        this.sizeY = sizeY;
        this.radius = radius;
        this.sizeX = sizeX;
    }


    public String getFigure() {
        return figure;
    }

    public void setFigure(String figure) {
        this.figure = figure;
    }
    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }
    public String getLayout() {
        return layout;
    }

    public void setLayout(String layout) {
        this.layout = layout;
    }
    public String getShapedata() {
        return shapeData;
    }

    public void setShapedata(String shapeData) {
        this.shapeData = shapeData;
    }
    public int getSizey() {
        return sizeY;
    }

    public void setSizey(int sizeY) {
        this.sizeY = sizeY;
    }
    public int getRadius() {
        return radius;
    }

    public void setRadius(int radius) {
        this.radius = radius;
    }
    public int getSizex() {
        return sizeX;
    }

    public void setSizex(int sizeX) {
        this.sizeX = sizeX;
    }


}