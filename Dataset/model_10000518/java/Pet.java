




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Pet  {

    private String email;
    private String breed;
    private LocalDate date;
    private String notes;
    private String place;
    private String color;
    private String state;
    private String picture;
    private int reward;
    private String phone;
    private boolean stray;
    private String chipID;
    private String type;
    private String name;



    public Pet(
        String email,        String breed,        LocalDate date,        String notes,        String place,        String color,        String state,        String picture,        int reward,        String phone,        boolean stray,        String chipID,        String type,        String name    ) {
        this.email = email;
        this.breed = breed;
        this.date = date;
        this.notes = notes;
        this.place = place;
        this.color = color;
        this.state = state;
        this.picture = picture;
        this.reward = reward;
        this.phone = phone;
        this.stray = stray;
        this.chipID = chipID;
        this.type = type;
        this.name = name;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getBreed() {
        return breed;
    }

    public void setBreed(String breed) {
        this.breed = breed;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }
    public String getPlace() {
        return place;
    }

    public void setPlace(String place) {
        this.place = place;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getPicture() {
        return picture;
    }

    public void setPicture(String picture) {
        this.picture = picture;
    }
    public int getReward() {
        return reward;
    }

    public void setReward(int reward) {
        this.reward = reward;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public boolean getStray() {
        return stray;
    }

    public void setStray(boolean stray) {
        this.stray = stray;
    }
    public String getChipid() {
        return chipID;
    }

    public void setChipid(String chipID) {
        this.chipID = chipID;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}