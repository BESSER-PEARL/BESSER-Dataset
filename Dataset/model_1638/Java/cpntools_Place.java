





import java.util.List;
import java.util.ArrayList;

public class cpntools_Place extends DiagramElement {

    private int height;
    private int width;
    private String text;





    private cpntools_Page cpntools_page;




    private cpntools_Page cpntools_page;




    private cpntools_Fusion cpntools_fusion;




    private cpntools_Fusion cpntools_fusion;


    public cpntools_Place(
        int height,        int width,        String text    ) {
        super(
        );
        this.height = height;
        this.width = width;
        this.text = text;
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
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public cpntools_Page getCpntools_page() {
        return cpntools_page;
    }

    public void setCpntools_page(cpntools_Page cpntools_page) {
        this.cpntools_page = cpntools_page;
    }
    public cpntools_Page getCpntools_page() {
        return cpntools_page;
    }

    public void setCpntools_page(cpntools_Page cpntools_page) {
        this.cpntools_page = cpntools_page;
    }
    public cpntools_Fusion getCpntools_fusion() {
        return cpntools_fusion;
    }

    public void setCpntools_fusion(cpntools_Fusion cpntools_fusion) {
        this.cpntools_fusion = cpntools_fusion;
    }
    public cpntools_Fusion getCpntools_fusion() {
        return cpntools_fusion;
    }

    public void setCpntools_fusion(cpntools_Fusion cpntools_fusion) {
        this.cpntools_fusion = cpntools_fusion;
    }

}