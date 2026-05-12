





import java.util.List;
import java.util.ArrayList;

public class plaetzchen  {

    private None pteig;
    private None pguss;
    private None pdeko;
    private String name;





    private teig teig;


    public plaetzchen(
        None pteig,        None pguss,        None pdeko,        String name    ) {
        this.pteig = pteig;
        this.pguss = pguss;
        this.pdeko = pdeko;
        this.name = name;
    }


    public None getPteig() {
        return pteig;
    }

    public void setPteig(None pteig) {
        this.pteig = pteig;
    }
    public None getPguss() {
        return pguss;
    }

    public void setPguss(None pguss) {
        this.pguss = pguss;
    }
    public None getPdeko() {
        return pdeko;
    }

    public void setPdeko(None pdeko) {
        this.pdeko = pdeko;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public teig getTeig() {
        return teig;
    }

    public void setTeig(teig teig) {
        this.teig = teig;
    }

}