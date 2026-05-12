





import java.util.List;
import java.util.ArrayList;

public class mapCarExchange  {

    private String timeExchange;
    private String mapOnCar;
    private int idCar;
    private int idMap;
    private String mapBelowCar;





    private Car car;


    public mapCarExchange(
        String timeExchange,        String mapOnCar,        int idCar,        int idMap,        String mapBelowCar    ) {
        this.timeExchange = timeExchange;
        this.mapOnCar = mapOnCar;
        this.idCar = idCar;
        this.idMap = idMap;
        this.mapBelowCar = mapBelowCar;
    }


    public String getTimeexchange() {
        return timeExchange;
    }

    public void setTimeexchange(String timeExchange) {
        this.timeExchange = timeExchange;
    }
    public String getMaponcar() {
        return mapOnCar;
    }

    public void setMaponcar(String mapOnCar) {
        this.mapOnCar = mapOnCar;
    }
    public int getIdcar() {
        return idCar;
    }

    public void setIdcar(int idCar) {
        this.idCar = idCar;
    }
    public int getIdmap() {
        return idMap;
    }

    public void setIdmap(int idMap) {
        this.idMap = idMap;
    }
    public String getMapbelowcar() {
        return mapBelowCar;
    }

    public void setMapbelowcar(String mapBelowCar) {
        this.mapBelowCar = mapBelowCar;
    }

    public Car getCar() {
        return car;
    }

    public void setCar(Car car) {
        this.car = car;
    }

}