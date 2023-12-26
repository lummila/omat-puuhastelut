using System;

class Pyramid
{
    public static void Main()
    {
        Console.Write("Enter amount of layers: ");
        int layerAmount = Convert.ToInt32(Console.ReadLine());

        List<string> result = PyramidBuilder(layerAmount);

        foreach (string x in result)
        {
            Console.WriteLine(x);
        }
    }

    public static List<string> PyramidBuilder(int layers)
    {
        List<string> output = new(layers);
        int blankSpace = layers * 2 - 1;

        for (int i = 0; i < layers; i++)
        {
            string str = "*";

            for (int y = 0; y < i; y++)
                str += "**";

            int spaces = blankSpace / 2 - i;
            if (spaces > 0)
                str = " ".PadLeft(spaces) + str + " ".PadLeft(spaces);

            output.Add(str);
        }

        return output;
    }
}
