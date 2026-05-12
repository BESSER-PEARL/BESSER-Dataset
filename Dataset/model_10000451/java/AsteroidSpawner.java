





import java.util.List;
import java.util.ArrayList;

public class AsteroidSpawner  {

    private float publicAttribute;
    private int privateAttribute;
    private String asteroids;
    private String packageAttribute;



    public AsteroidSpawner(
        float publicAttribute,        int privateAttribute,        String asteroids,        String packageAttribute    ) {
        this.publicAttribute = publicAttribute;
        this.privateAttribute = privateAttribute;
        this.asteroids = asteroids;
        this.packageAttribute = packageAttribute;
    }


    public float getPublicattribute() {
        return publicAttribute;
    }

    public void setPublicattribute(float publicAttribute) {
        this.publicAttribute = publicAttribute;
    }
    public int getPrivateattribute() {
        return privateAttribute;
    }

    public void setPrivateattribute(int privateAttribute) {
        this.privateAttribute = privateAttribute;
    }
    public String getAsteroids() {
        return asteroids;
    }

    public void setAsteroids(String asteroids) {
        this.asteroids = asteroids;
    }
    public String getPackageattribute() {
        return packageAttribute;
    }

    public void setPackageattribute(String packageAttribute) {
        this.packageAttribute = packageAttribute;
    }


}