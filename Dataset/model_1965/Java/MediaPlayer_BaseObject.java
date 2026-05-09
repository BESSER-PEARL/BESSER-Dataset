





import java.util.List;
import java.util.ArrayList;

public class MediaPlayer_BaseObject  {

    private int id;
    private String propertyChangeSupport;



    public MediaPlayer_BaseObject(
        int id,        String propertyChangeSupport    ) {
        this.id = id;
        this.propertyChangeSupport = propertyChangeSupport;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getPropertychangesupport() {
        return propertyChangeSupport;
    }

    public void setPropertychangesupport(String propertyChangeSupport) {
        this.propertyChangeSupport = propertyChangeSupport;
    }


}