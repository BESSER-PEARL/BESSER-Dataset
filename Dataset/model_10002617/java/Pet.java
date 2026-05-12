




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Pet  {

    private boolean stray;
    private String breed;
    private String phone;
    private String color;
    private String notes;
    private String picture;
    private String email;
    private String state;
    private int reward;
    private LocalDate date;
    private String chipID;
    private String name;
    private String place;
    private String type;



    public Pet(
        boolean stray,        String breed,        String phone,        String color,        String notes,        String picture,        String email,        String state,        int reward,        LocalDate date,        String chipID,        String name,        String place,        String type    ) {
        this.stray = stray;
        this.breed = breed;
        this.phone = phone;
        this.color = color;
        this.notes = notes;
        this.picture = picture;
        this.email = email;
        this.state = state;
        this.reward = reward;
        this.date = date;
        this.chipID = chipID;
        this.name = name;
        this.place = place;
        this.type = type;
    }


    public boolean getStray() {
        return stray;
    }

    public void setStray(boolean stray) {
        this.stray = stray;
    }
    public String getBreed() {
        return breed;
    }

    public void setBreed(String breed) {
        this.breed = breed;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }
    public String getPicture() {
        return picture;
    }

    public void setPicture(String picture) {
        this.picture = picture;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public int getReward() {
        return reward;
    }

    public void setReward(int reward) {
        this.reward = reward;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getChipid() {
        return chipID;
    }

    public void setChipid(String chipID) {
        this.chipID = chipID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPlace() {
        return place;
    }

    public void setPlace(String place) {
        this.place = place;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}