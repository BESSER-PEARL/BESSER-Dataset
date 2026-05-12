





import java.util.List;
import java.util.ArrayList;

public class maps_map  {

    private String size;
    private String country;
    private String name;
    private boolean isCity;





    private List<maps_PublicSpace> maps_publicspaces;


    public maps_map(
        String size,        String country,        String name,        boolean isCity    ) {
        this.size = size;
        this.country = country;
        this.name = name;
        this.isCity = isCity;
        this.maps_publicspaces = new ArrayList<>();
    }

    public maps_map(
        String size,        String country,        String name,        boolean isCity        ArrayList<maps_PublicSpace> maps_publicspaces    ) {
        this.size = size;
        this.country = country;
        this.name = name;
        this.isCity = isCity;
        this.maps_publicspaces = maps_publicspaces;
    }

    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIscity() {
        return isCity;
    }

    public void setIscity(boolean isCity) {
        this.isCity = isCity;
    }

    public List<maps_PublicSpace> getMaps_publicspaces() {
        return maps_publicspaces;
    }

    public void addMaps_publicspace(Maps_publicspace maps_publicspace) {
        this.maps_publicspaces.add(maps_publicspace);
    }

}