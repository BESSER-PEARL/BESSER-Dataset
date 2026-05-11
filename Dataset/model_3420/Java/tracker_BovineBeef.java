





import java.util.List;
import java.util.ArrayList;

public class tracker_BovineBeef extends Bovine {

    private String beefBreed;



    public tracker_BovineBeef(
        String beefBreed    ) {
        super(
        );
        this.beefBreed = beefBreed;
    }


    public String getBeefbreed() {
        return beefBreed;
    }

    public void setBeefbreed(String beefBreed) {
        this.beefBreed = beefBreed;
    }


}