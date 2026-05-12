




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Pet  {

    private String state;
    private String phone;
    private String place;
    private boolean stray;
    private String color;
    private int reward;
    private String name;
    private String breed;
    private LocalDate date;
    private String type;
    private String picture;
    private String email;
    private String chipID;
    private String notes;



    public Pet(
        String state,        String phone,        String place,        boolean stray,        String color,        int reward,        String name,        String breed,        LocalDate date,        String type,        String picture,        String email,        String chipID,        String notes    ) {
        this.state = state;
        this.phone = phone;
        this.place = place;
        this.stray = stray;
        this.color = color;
        this.reward = reward;
        this.name = name;
        this.breed = breed;
        this.date = date;
        this.type = type;
        this.picture = picture;
        this.email = email;
        this.chipID = chipID;
        this.notes = notes;
    }


    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getPlace() {
        return place;
    }

    public void setPlace(String place) {
        this.place = place;
    }
    public boolean getStray() {
        return stray;
    }

    public void setStray(boolean stray) {
        this.stray = stray;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public int getReward() {
        return reward;
    }

    public void setReward(int reward) {
        this.reward = reward;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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
    public String getChipid() {
        return chipID;
    }

    public void setChipid(String chipID) {
        this.chipID = chipID;
    }
    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }


}