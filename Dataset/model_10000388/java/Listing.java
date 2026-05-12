





import java.util.List;
import java.util.ArrayList;

public class Listing  {

    private int numberOfBedroms;
    private int numberOfBathrooms;
    private String image;
    private int livingRooom;
    private String video;
    private int parkingPossibilities;
    private int kitchen;
    private String address;
    private boolean furnished;





    private Actor actor;


    public Listing(
        int numberOfBedroms,        int numberOfBathrooms,        String image,        int livingRooom,        String video,        int parkingPossibilities,        int kitchen,        String address,        boolean furnished    ) {
        this.numberOfBedroms = numberOfBedroms;
        this.numberOfBathrooms = numberOfBathrooms;
        this.image = image;
        this.livingRooom = livingRooom;
        this.video = video;
        this.parkingPossibilities = parkingPossibilities;
        this.kitchen = kitchen;
        this.address = address;
        this.furnished = furnished;
    }


    public int getNumberofbedroms() {
        return numberOfBedroms;
    }

    public void setNumberofbedroms(int numberOfBedroms) {
        this.numberOfBedroms = numberOfBedroms;
    }
    public int getNumberofbathrooms() {
        return numberOfBathrooms;
    }

    public void setNumberofbathrooms(int numberOfBathrooms) {
        this.numberOfBathrooms = numberOfBathrooms;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public int getLivingrooom() {
        return livingRooom;
    }

    public void setLivingrooom(int livingRooom) {
        this.livingRooom = livingRooom;
    }
    public String getVideo() {
        return video;
    }

    public void setVideo(String video) {
        this.video = video;
    }
    public int getParkingpossibilities() {
        return parkingPossibilities;
    }

    public void setParkingpossibilities(int parkingPossibilities) {
        this.parkingPossibilities = parkingPossibilities;
    }
    public int getKitchen() {
        return kitchen;
    }

    public void setKitchen(int kitchen) {
        this.kitchen = kitchen;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public boolean getFurnished() {
        return furnished;
    }

    public void setFurnished(boolean furnished) {
        this.furnished = furnished;
    }

    public Actor getActor() {
        return actor;
    }

    public void setActor(Actor actor) {
        this.actor = actor;
    }

}