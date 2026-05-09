





import java.util.List;
import java.util.ArrayList;

public class cpntools_Trans extends DiagramElement {

    private int height;
    private int width;
    private boolean explicit;
    private String text;





    private cpntools_Page cpntools_page;




    private cpntools_Page cpntools_page;


    public cpntools_Trans(
        int height,        int width,        boolean explicit,        String text    ) {
        super(
        );
        this.height = height;
        this.width = width;
        this.explicit = explicit;
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
    public boolean getExplicit() {
        return explicit;
    }

    public void setExplicit(boolean explicit) {
        this.explicit = explicit;
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

}