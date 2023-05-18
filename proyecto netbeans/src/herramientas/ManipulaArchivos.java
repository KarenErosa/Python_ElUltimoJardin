/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package herramientas;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutput;
import java.io.ObjectOutputStream;
import java.util.ArrayList;

/**
 *
 * @author Equipo 4
 */
public class ManipulaArchivos
{
    public static void guarda(String s, Object o)
    {
        try
        {
            FileOutputStream fis=new FileOutputStream(s);
            ObjectOutputStream arch=new ObjectOutputStream(fis);
            arch.writeObject(o);
            arch.close();
        } catch (Exception e)
        {
            System.out.println("Error..." + e.toString());
        }
    }
    
    public static void guarda(String s, ArrayList o)
    {
        try
        {
            FileOutputStream fis=new FileOutputStream(s);
            ObjectOutputStream arch=new ObjectOutputStream(fis);
            arch.writeObject(o);
            arch.close();
        } catch (Exception e)
        {
            System.out.println("Error..." + e.toString());
        }
    }
    
    public static void guarda(String s,Object o[])
    {
        try
        {
            FileOutputStream fis=new FileOutputStream(s);
            ObjectOutputStream arch=new ObjectOutputStream(fis);
            arch.writeObject(o);
            arch.close();
        } catch (Exception e)
        {
            System.out.println("Error..." + e.toString());
        }
    }
    public static void guarda(String s,Object o[][])
    {
        try
        {
            FileOutputStream fis=new FileOutputStream(s);
            ObjectOutputStream arch=new ObjectOutputStream(fis);
            arch.writeObject(o);
            arch.close();
        } catch (Exception e)
        {
            System.out.println("Error..." + e.toString());
        }
    }
    public static ArrayList carga(String s)
    {
        ArrayList o = new ArrayList();
        try
        {
            FileInputStream fis=new FileInputStream(s);
            ObjectInputStream arch=new ObjectInputStream(fis);
            o=(ArrayList)arch.readObject();
            arch.close();
        } catch (Exception e)
        {
            System.out.println("Error.."+ e.toString());
        }
        return o;
    }
    public static Object cargaMatriz(String s)
    {
        Object o[][]=null;
        try
        {
            FileInputStream fis=new FileInputStream(s);
            ObjectInputStream arch=new ObjectInputStream(fis);
            o=(Object[][])arch.readObject();
            arch.close();
        } catch (Exception e)
        {
            System.out.println("Error.."+ e.toString());
        }
        return o;
    }
    public static Object [] carga(String s,boolean b)
    {
        Object o[]=null;
        try
        {
            FileInputStream fis=new FileInputStream(s);
            ObjectInputStream arch=new ObjectInputStream(fis);
            o=(Object[])arch.readObject();
            arch.close();
        } catch (Exception e)
        {
            System.out.println("Error.."+ e.toString());
        }
        return o;
    }

    public static Object cargaNum(String s)
    {
        Object o=null;
        try
        {
            FileInputStream fis=new FileInputStream(s);
            ObjectInputStream arch=new ObjectInputStream(fis);
            o= arch.readObject();
            arch.close();
        } catch (Exception e)
        {
            System.out.println("Error.."+ e.toString());
        }
        return o;
    }
}
