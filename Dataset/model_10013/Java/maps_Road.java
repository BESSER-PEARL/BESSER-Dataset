





import java.util.List;
import java.util.ArrayList;

public class maps_Road  {

    private String district;
    private String name;
    private int length;





    private List<maps_PublicSpace> maps_publicspaces;




    private maps_map maps_map;




    private maps_PublicSpace maps_publicspace;




    private maps_Road maps_road;


    public maps_Road(
        String district,        String name,        int length    ) {
        this.district = district;
        this.name = name;
        this.length = length;
        this.maps_publicspaces = new ArrayList<>();
    }

    public maps_Road(
        String district,        String name,        int length        ArrayList<maps_PublicSpace> maps_publicspaces    ) {
        this.district = district;
        this.name = name;
        this.length = length;
        this.maps_publicspaces = maps_publicspaces;
    }

    public String getDistrict() {
        return district;
    }

    public void setDistrict(String district) {
        this.district = district;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }

    public List<maps_PublicSpace> getMaps_publicspaces() {
        return maps_publicspaces;
    }

    public void addMaps_publicspace(Maps_publicspace maps_publicspace) {
        this.maps_publicspaces.add(maps_publicspace);
    }
    public maps_map getMaps_map() {
        return maps_map;
    }

    public void setMaps_map(maps_map maps_map) {
        this.maps_map = maps_map;
    }
    public maps_PublicSpace getMaps_publicspace() {
        return maps_publicspace;
    }

    public void setMaps_publicspace(maps_PublicSpace maps_publicspace) {
        this.maps_publicspace = maps_publicspace;
    }
    public maps_Road getMaps_road() {
        return maps_road;
    }

    public void setMaps_road(maps_Road maps_road) {
        this.maps_road = maps_road;
    }

}