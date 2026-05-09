





import java.util.List;
import java.util.ArrayList;

public class cpntools_Arc extends DiagramElement {

    private String orientation;
    private int order;
    private float headsize;
    private String currentcyckle;





    private cpntools_Place cpntools_place;




    private cpntools_Trans cpntools_trans;




    private cpntools_Page cpntools_page;




    private cpntools_Place cpntools_place;




    private cpntools_Trans cpntools_trans;




    private cpntools_Page cpntools_page;


    public cpntools_Arc(
        String orientation,        int order,        float headsize,        String currentcyckle    ) {
        super(
        );
        this.orientation = orientation;
        this.order = order;
        this.headsize = headsize;
        this.currentcyckle = currentcyckle;
    }


    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }
    public int getOrder() {
        return order;
    }

    public void setOrder(int order) {
        this.order = order;
    }
    public float getHeadsize() {
        return headsize;
    }

    public void setHeadsize(float headsize) {
        this.headsize = headsize;
    }
    public String getCurrentcyckle() {
        return currentcyckle;
    }

    public void setCurrentcyckle(String currentcyckle) {
        this.currentcyckle = currentcyckle;
    }

    public cpntools_Place getCpntools_place() {
        return cpntools_place;
    }

    public void setCpntools_place(cpntools_Place cpntools_place) {
        this.cpntools_place = cpntools_place;
    }
    public cpntools_Trans getCpntools_trans() {
        return cpntools_trans;
    }

    public void setCpntools_trans(cpntools_Trans cpntools_trans) {
        this.cpntools_trans = cpntools_trans;
    }
    public cpntools_Page getCpntools_page() {
        return cpntools_page;
    }

    public void setCpntools_page(cpntools_Page cpntools_page) {
        this.cpntools_page = cpntools_page;
    }
    public cpntools_Place getCpntools_place() {
        return cpntools_place;
    }

    public void setCpntools_place(cpntools_Place cpntools_place) {
        this.cpntools_place = cpntools_place;
    }
    public cpntools_Trans getCpntools_trans() {
        return cpntools_trans;
    }

    public void setCpntools_trans(cpntools_Trans cpntools_trans) {
        this.cpntools_trans = cpntools_trans;
    }
    public cpntools_Page getCpntools_page() {
        return cpntools_page;
    }

    public void setCpntools_page(cpntools_Page cpntools_page) {
        this.cpntools_page = cpntools_page;
    }

}