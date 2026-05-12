





import java.util.List;
import java.util.ArrayList;

public class PERSONNEL  {

    private String prenomPersonnel;
    private String nomPersonnel;
    private boolean unPrivate;



    public PERSONNEL(
        String prenomPersonnel,        String nomPersonnel,        boolean unPrivate    ) {
        this.prenomPersonnel = prenomPersonnel;
        this.nomPersonnel = nomPersonnel;
        this.unPrivate = unPrivate;
    }


    public String getPrenompersonnel() {
        return prenomPersonnel;
    }

    public void setPrenompersonnel(String prenomPersonnel) {
        this.prenomPersonnel = prenomPersonnel;
    }
    public String getNompersonnel() {
        return nomPersonnel;
    }

    public void setNompersonnel(String nomPersonnel) {
        this.nomPersonnel = nomPersonnel;
    }
    public boolean getUnprivate() {
        return unPrivate;
    }

    public void setUnprivate(boolean unPrivate) {
        this.unPrivate = unPrivate;
    }


}