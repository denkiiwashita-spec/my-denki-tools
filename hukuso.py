import cmath

def complex_calculator():
    print("--- 電験2種対応：複素数計算ツール ---")
    print("入力例: 3+4j (直交形式) / 5,53.1 (極形式: 絶対値,角度度数)")
    
    try:
        # 入力を取得
        inp = input("計算式、または値を入力してください: ")
        
        # 極形式（r,deg）の入力を複素数に変換する処理
        if "," in inp:
            r, deg = map(float, inp.split(","))
            # 度数をラジアンに変換して複素数化
            z = cmath.rect(r, math.radians(deg))
        else:
            # 直接 3+4j などの形式を読み込む
            z = complex(inp.replace('i', 'j')) # iでも入力できるように

        # 各種形式で出力
        r, phi = cmath.polar(z)
        deg = cmath.degrees(phi)

        print("-" * 30)
        print(f"【直交形式】 {z.real:.4f} + j{z.imag:.4f}")
        print(f"【極形式】   絶対値: {r:.4f}, 角度: {deg:.2f}°")
        print(f"【共役複素数】 {z.conjugate().real:.4f} - j{z.conjugate().imag:.4f}")
        print("-" * 30)

    except Exception as e:
        print(f"入力エラー: {e}")

if __name__ == "__main__":
    import math
    complex_calculator()