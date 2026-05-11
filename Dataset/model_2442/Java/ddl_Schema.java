





import java.util.List;
import java.util.ArrayList;

public class ddl_Schema extends DataElement {

    private int version;
    private boolean conformite;
    private float prix;



    public ddl_Schema(
        int version,        boolean conformite,        float prix    ) {
        super(
        );
        this.version = version;
        this.conformite = conformite;
        this.prix = prix;
    }


    public int getVersion() {
        return version;
    }

    public void setVersion(int version) {
        this.version = version;
    }
    public boolean getConformite() {
        return conformite;
    }

    public void setConformite(boolean conformite) {
        this.conformite = conformite;
    }
    public float getPrix() {
        return prix;
    }

    public void setPrix(float prix) {
        this.prix = prix;
    }


}