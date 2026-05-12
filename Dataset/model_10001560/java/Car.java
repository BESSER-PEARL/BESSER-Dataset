





import java.util.List;
import java.util.ArrayList;

public class Car  {

    private String fareCar;
    private int statusCar;
    private String mapOnCar;
    private String numberPlatesCar;
    private String imageLinkCar;
    private String phoneCar;
    private String nameCar;
    private String positionEndCar;
    private String timeStartCar;
    private String mapBelowCar;
    private int idUser;
    private int classifyCar;
    private int idCar;
    private String positionStartCar;



    public Car(
        String fareCar,        int statusCar,        String mapOnCar,        String numberPlatesCar,        String imageLinkCar,        String phoneCar,        String nameCar,        String positionEndCar,        String timeStartCar,        String mapBelowCar,        int idUser,        int classifyCar,        int idCar,        String positionStartCar    ) {
        this.fareCar = fareCar;
        this.statusCar = statusCar;
        this.mapOnCar = mapOnCar;
        this.numberPlatesCar = numberPlatesCar;
        this.imageLinkCar = imageLinkCar;
        this.phoneCar = phoneCar;
        this.nameCar = nameCar;
        this.positionEndCar = positionEndCar;
        this.timeStartCar = timeStartCar;
        this.mapBelowCar = mapBelowCar;
        this.idUser = idUser;
        this.classifyCar = classifyCar;
        this.idCar = idCar;
        this.positionStartCar = positionStartCar;
    }


    public String getFarecar() {
        return fareCar;
    }

    public void setFarecar(String fareCar) {
        this.fareCar = fareCar;
    }
    public int getStatuscar() {
        return statusCar;
    }

    public void setStatuscar(int statusCar) {
        this.statusCar = statusCar;
    }
    public String getMaponcar() {
        return mapOnCar;
    }

    public void setMaponcar(String mapOnCar) {
        this.mapOnCar = mapOnCar;
    }
    public String getNumberplatescar() {
        return numberPlatesCar;
    }

    public void setNumberplatescar(String numberPlatesCar) {
        this.numberPlatesCar = numberPlatesCar;
    }
    public String getImagelinkcar() {
        return imageLinkCar;
    }

    public void setImagelinkcar(String imageLinkCar) {
        this.imageLinkCar = imageLinkCar;
    }
    public String getPhonecar() {
        return phoneCar;
    }

    public void setPhonecar(String phoneCar) {
        this.phoneCar = phoneCar;
    }
    public String getNamecar() {
        return nameCar;
    }

    public void setNamecar(String nameCar) {
        this.nameCar = nameCar;
    }
    public String getPositionendcar() {
        return positionEndCar;
    }

    public void setPositionendcar(String positionEndCar) {
        this.positionEndCar = positionEndCar;
    }
    public String getTimestartcar() {
        return timeStartCar;
    }

    public void setTimestartcar(String timeStartCar) {
        this.timeStartCar = timeStartCar;
    }
    public String getMapbelowcar() {
        return mapBelowCar;
    }

    public void setMapbelowcar(String mapBelowCar) {
        this.mapBelowCar = mapBelowCar;
    }
    public int getIduser() {
        return idUser;
    }

    public void setIduser(int idUser) {
        this.idUser = idUser;
    }
    public int getClassifycar() {
        return classifyCar;
    }

    public void setClassifycar(int classifyCar) {
        this.classifyCar = classifyCar;
    }
    public int getIdcar() {
        return idCar;
    }

    public void setIdcar(int idCar) {
        this.idCar = idCar;
    }
    public String getPositionstartcar() {
        return positionStartCar;
    }

    public void setPositionstartcar(String positionStartCar) {
        this.positionStartCar = positionStartCar;
    }


}