





import java.util.List;
import java.util.ArrayList;

public class di_Shape extends ContainerShape {

    private int x;
    private int height;
    private int width;
    private int y;





    private di_ContainerShape di_containershape;




    private List<di_Link> di_links;




    private di_Link di_link;




    private di_Link di_link;




    private List<di_Link> di_links;


    public di_Shape(
        int x,        int height,        int width,        int y    ) {
        super(
        );
        this.x = x;
        this.height = height;
        this.width = width;
        this.y = y;
        this.di_links = new ArrayList<>();
        this.di_links = new ArrayList<>();
    }

    public di_Shape(
        int x,        int height,        int width,        int y        ArrayList<di_Link> di_links,        ArrayList<di_Link> di_links    ) {
        this.x = x;
        this.height = height;
        this.width = width;
        this.y = y;
        this.di_links = di_links;
        this.di_links = di_links;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public di_ContainerShape getDi_containershape() {
        return di_containershape;
    }

    public void setDi_containershape(di_ContainerShape di_containershape) {
        this.di_containershape = di_containershape;
    }
    public List<di_Link> getDi_links() {
        return di_links;
    }

    public void addDi_link(Di_link di_link) {
        this.di_links.add(di_link);
    }
    public di_Link getDi_link() {
        return di_link;
    }

    public void setDi_link(di_Link di_link) {
        this.di_link = di_link;
    }
    public di_Link getDi_link() {
        return di_link;
    }

    public void setDi_link(di_Link di_link) {
        this.di_link = di_link;
    }
    public List<di_Link> getDi_links() {
        return di_links;
    }

    public void addDi_link(Di_link di_link) {
        this.di_links.add(di_link);
    }

}