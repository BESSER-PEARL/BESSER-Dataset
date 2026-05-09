





import java.util.List;
import java.util.ArrayList;

public class sunBooks_DocumentRoot  {

    private String mixed;





    private List<sunBooks_CollectionType> sunbooks_collectiontypes;


    public sunBooks_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.sunbooks_collectiontypes = new ArrayList<>();
    }

    public sunBooks_DocumentRoot(
        String mixed        ArrayList<sunBooks_CollectionType> sunbooks_collectiontypes    ) {
        this.mixed = mixed;
        this.sunbooks_collectiontypes = sunbooks_collectiontypes;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<sunBooks_CollectionType> getSunbooks_collectiontypes() {
        return sunbooks_collectiontypes;
    }

    public void addSunbooks_collectiontype(Sunbooks_collectiontype sunbooks_collectiontype) {
        this.sunbooks_collectiontypes.add(sunbooks_collectiontype);
    }

}