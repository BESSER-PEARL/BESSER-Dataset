





import java.util.List;
import java.util.ArrayList;

public class afpText_TileSize extends triplet {

    private String TVSIZE;
    private String THSIZE;
    private String RELRES;



    public afpText_TileSize(
        String TVSIZE,        String THSIZE,        String RELRES    ) {
        super(
        );
        this.TVSIZE = TVSIZE;
        this.THSIZE = THSIZE;
        this.RELRES = RELRES;
    }


    public String getTvsize() {
        return TVSIZE;
    }

    public void setTvsize(String TVSIZE) {
        this.TVSIZE = TVSIZE;
    }
    public String getThsize() {
        return THSIZE;
    }

    public void setThsize(String THSIZE) {
        this.THSIZE = THSIZE;
    }
    public String getRelres() {
        return RELRES;
    }

    public void setRelres(String RELRES) {
        this.RELRES = RELRES;
    }


}